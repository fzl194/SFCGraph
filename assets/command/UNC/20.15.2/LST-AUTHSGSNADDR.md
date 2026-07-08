---
id: UNC@20.15.2@MMLCommand@LST AUTHSGSNADDR
type: MMLCommand
name: LST AUTHSGSNADDR（查询向AAA鉴权服务器发送消息中携带的地址信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AUTHSGSNADDR
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 鉴权管理
- 服务节点地址信息
status: active
---

# LST AUTHSGSNADDR（查询向AAA鉴权服务器发送消息中携带的地址信息）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用来查询SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元的配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTHSGSNADDR]] · 向AAA鉴权服务器发送消息中携带的地址信息（AUTHSGSNADDR）

## 使用实例

查询SPW-C和PGW-C向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元的配置 ：

```
%%LST AUTHSGSNADDR:;%%
RETCODE = 0  操作成功

结果如下
--------
3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元中携带的地址信息  =  Pa接口
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询向AAA鉴权服务器发送消息中携带的地址信息（LST-AUTHSGSNADDR）_96242089.md`
