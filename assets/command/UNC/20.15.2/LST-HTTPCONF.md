---
id: UNC@20.15.2@MMLCommand@LST HTTPCONF
type: MMLCommand
name: LST HTTPCONF（查询HTTP属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPCONF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP属性管理
status: active
---

# LST HTTPCONF（查询HTTP属性）

## 功能

该命令用于查询HTTP协议层的属性配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPCONF]] · HTTP属性（HTTPCONF）

## 使用实例

如果想查询HTTP协议层的属性配置，可以用如下命令：

```
%%LST HTTPCONF:;%%
RETCODE = 0  操作成功

结果如下
--------
                       信令路由开关  =  否
                http-server日志级别  =  ERROR
                tcp-process日志级别  =  FATAL
        故障链路探测最长时间间隔(s)  =  720
            链路负载上报时间间隔(s)  =  10
                  链路老化时间(min)  =  10
  客户端接收HTTP响应消息超时时间(s)  =  5
服务端接收HTTP请求消息体超时时间(s)  =  3
  服务端回复HTTP响应消息超时时间(s)  =  5
            客户端HTTP PING探测开关  =  是
     客户端HTTP PING探测时间间隔(s)  =  60
            客户端HTTP PING探测次数  =  3
                               描述  =  NULL
                  Keepalive功能开关  =  打开
               Keepalive空闲时间(s)  =  1800
               Keepalive探测间隔(s)  =  5
                  Keepalive探测次数  =  5
             最大消息体大小(MBytes)  =  2
           JSON数据最多叶子节点个数  =  16000
             TCP会话删除延迟时间(s)  =  3
                   客户端最大并发流  =  0
                 初始重建链间隔(ms)  =  200
           IP可达自动探测的功能开关  =  是
                   性能统计功能开关  =  是
   发送恢复链路集信息请求的时间间隔  =  30
                       配置核查开关  =  是
                       链路核查开关  =  是
              压缩报文阈值 (KBytes)  =  60
                      Reqcb流控开关  =  是
          TCP SYN包重传时间间隔(ms)  =  500
              TCP SYN包重传最大次数  =  0
        TCP建链成功后包重传最大次数  =  12
       HTTP建链自动退避时间间隔(ms)  =  100
                    使能HTTP1.1开关  =  否
                HTTP Goaway处理开关  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPCONF.md`
