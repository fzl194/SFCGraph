---
id: UNC@20.15.2@MMLCommand@LST UPFRDSSVR
type: MMLCommand
name: LST UPFRDSSVR（查询中转UPF与Radius服务器的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFRDSSVR
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- UPF中转Radius服务器
status: active
---

# LST UPFRDSSVR（查询中转UPF与Radius服务器的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

查询中转UPF与Radius服务器的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERTYPE | 服务器类型 | 可选必选说明：可选参数<br>参数含义：指定RADIUS服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（鉴权服务器）”：表示鉴权服务器。<br>- “ACCOUNTING（计费服务器）”：表示计费服务器。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFRDSSVR]] · 中转UPF与Radius服务器的绑定关系（UPFRDSSVR）

## 使用实例

显示计费服务器的配置信息：

```
LST UPFRDSSVR:;
RETCODE = 0  操作成功

结果如下
--------
服务器类型  服务器IP版本  IPv4地址      UP列表名称

计费服务器  IPv4          192.168.10.1  uplist2
计费服务器  IPv4          192.168.0.47  up1
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询中转UPF与Radius服务器的绑定关系（LST-UPFRDSSVR）_88248952.md`
