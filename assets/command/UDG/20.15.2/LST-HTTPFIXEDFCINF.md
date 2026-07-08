---
id: UDG@20.15.2@MMLCommand@LST HTTPFIXEDFCINF
type: MMLCommand
name: LST HTTPFIXEDFCINF（查询HTTP接口类型固定速率流控信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPFIXEDFCINF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP接口类型固定速率流控管理
status: active
---

# LST HTTPFIXEDFCINF（查询HTTP接口类型固定速率流控信息）

## 功能

该命令用于查询HTTP接口类型固定速率流控门限值信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LETYPE | 本端实体类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体的类型。<br>数据来源：全网规划<br>取值范围：<br>- “SERVER（服务端）”：服务端<br>- “CLIENT（客户端）”：客户端<br>默认值：无<br>配置原则：<br>HTTP本端实体可以作为服务端也可以作为客户端，两者需要分别配置。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HTTPFIXEDFCINF]] · HTTP接口类型固定速率流控信息（HTTPFIXEDFCINF）

## 使用实例

- 查询本端实体类型为服务端的HTTP接口类型固定速率流控门限值信息，可以用以下命令：
  ```
  %%LST HTTPFIXEDFCINF: LETYPE=SERVER;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                   局向索引 = 1
               本端实体类型 = 服务端
    接收消息流控门限(条/秒) = 600
                     状态码 = Too Many Requests
  是否携带Retry-After消息头 = YES
        Retry-After时长(秒) = 180
  (结果个数 = 1)

  ---    END
  ```
- 查询本端实体类型为客户端的HTTP接口类型固定速率流控门限值信息，可以用以下命令：
  ```
  %%LST HTTPFIXEDFCINF: LETYPE=CLIENT;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                   局向索引 = 2
               本端实体类型 = 客户端
    发送消息流控门限(条/秒) = 600
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HTTPFIXEDFCINF.md`
