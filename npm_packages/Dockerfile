FROM node:16.13.1

RUN npm install -g @angular/cli
RUN mkdir /ng-app

WORKDIR /ng-app
COPY ./ ./



RUN yarn

RUN ng build lib1
RUN ng build lib2
RUN ng build lib3

RUN cp ./.npmrc_push ./dist/lib1/.npmrc
RUN cp ./.npmrc_push ./dist/lib1/.npmrc
RUN cp ./.npmrc_push ./dist/lib1/.npmrc

#3. push libraries to the npm
RUN cd /ng-app/dist/lib1
WORKDIR /ng-app/dist/lib1
RUN npm publish --tag latest
WORKDIR /ng-app/dist/lib2
RUN cd /ng-app/dist/lib2 && npm publish --tag latest
WORKDIR /ng-app/dist/lib3
RUN cd /ng-app/dist/lib3 && npm publish --tag latest
