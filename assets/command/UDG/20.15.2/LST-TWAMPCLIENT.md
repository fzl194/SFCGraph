---
id: UDG@20.15.2@MMLCommand@LST TWAMPCLIENT
type: MMLCommand
name: LST TWAMPCLIENT（查询TWAMP客户端）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TWAMPCLIENT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP客户端配置
status: active
---

# LST TWAMPCLIENT（查询TWAMP客户端）

## 功能

该命令用于查询TWAMP客户端。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTID | 客户端ID | 可选必选说明：可选参数<br>参数含义：该参数用于配置客户端ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~12000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TWAMPCLIENT]] · TWAMP客户端（TWAMPCLIENT）

## 使用实例

查询客户端ID为1的实例：

```
%%LST TWAMPCLIENT: CLIENTID=1;%%
RETCODE = 0  操作成功

结果如下
--------
       客户端ID  =  1
      TWAMP架构  =  LIGHT
      地址族类型  =  IPV4
    本端IPV4地址  =  10.0.0.0
    对端IPV4地址  =  192.168.0.0
     本端UDP端口  =  65450
     对端UDP端口  =  1
      差分服务码  =  0
     VPN实例名称  =  ck
            描述  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TWAMPCLIENT.md`
