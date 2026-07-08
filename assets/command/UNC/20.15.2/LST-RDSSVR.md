---
id: UNC@20.15.2@MMLCommand@LST RDSSVR
type: MMLCommand
name: LST RDSSVR（查询RADIUS服务器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSSVR
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- Radius服务器
status: active
---

# LST RDSSVR（查询RADIUS服务器）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询RADIUS服务器组下的RADIUS服务器的相关信息。如果不指定可选参数，该命令将显示所有RADIUS服务器组下的RADIUS服务器配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：可选参数<br>参数含义：指定RADIUS服务器所属RADIUS服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不允许输入空格。<br>默认值：无<br>配置原则：输入RDSSVRGRPNAME时查询指定RADIUS服务器组下的服务器信息，不输入查询全部RADIUS服务器组下的服务器信息。 |
| SERVERTYPE | 服务器类型 | 可选必选说明：可选参数<br>参数含义：指定RADIUS服务器类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AUTHENTICATION：鉴权服务器。<br>- ACCOUNTING：计费服务器。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSSVR]] · RADIUS服务器（RDSSVR）

## 使用实例

显示组名为“rdssvr”的RADIUS服务器组下的计费服务器的配置信息：

```
LST RDSSVR: RDSSVRGRPNAME="rdssvr", SERVERTYPE=ACCOUNTING;
```

```

RETCODE = 0  操作成功

RADIUS服务器
------------
RADIUS Server Group名称  =  rdssvr
             服务器类型  =  计费服务器
                   端口  =  2020
                VPN实例  =  NULL
   服务器密钥（加密的）  =  *****
       小区拥塞上报开关  =  不支持。
             主备用类型  =  主服务器
           服务器优先级  =  0
                  wal值  =  0
 Radius计费消息属性模板  =  NULL
                 IP地址  =  192.168.10.1
             UP列表名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RADIUS服务器（LST-RDSSVR）_09896759.md`
