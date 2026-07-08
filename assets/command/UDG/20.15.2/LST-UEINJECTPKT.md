---
id: UDG@20.15.2@MMLCommand@LST UEINJECTPKT
type: MMLCommand
name: LST UEINJECTPKT（查询UE灌包参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UEINJECTPKT
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包参数
status: active
---

# LST UEINJECTPKT（查询UE灌包参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询UE下行灌包功能的UE灌包参数。

## 注意事项

若不指定UE下行灌包用户的imsi，msisdn或imei，则查询已配置的所有UE下行灌包参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用于指定用户标识为IMSI。<br>- MSISDN：用于指定用户标识为MSISDN。<br>- IMEI：用于指定用户标识为IMEI。<br>默认值：无<br>配置原则：无 |
| USERIDINFO | 用户ID信息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IMSI”、“MSISDN” 或 “IMEI”时为必选参数。<br>参数含义：该参数用于指定用户ID信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。1、当用户ID类型为IMSI时，长度范围是1～15，每个字符必须为0~9的数字。 2、当用户ID类型为MSISDN时，长度范围是1～15，每个字符必须为0~9的数字。 3、当用户ID类型为IMEI时，长度范围是1～16，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEINJECTPKT]] · UE灌包参数（UEINJECTPKT）

## 使用实例

查询UE下行灌包功能的UE灌包参数：

```
LST UEINJECTPKT:;
```

```

RETCODE = 0  操作成功。

UE 下行灌包参数信息
-------------------
     IP 类型  =  IPv4
报文净荷长度  =  1500
    报文内容  =  34df
    灌包数量  =  0
    灌包时长  =  50
    灌包速率  =  2000
      源端口  =  2001
    目的端口  =  2001
    用户标识  =  IMSI
  用户ID信息  =  12345678901234
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询UE灌包参数（LST-UEINJECTPKT）_82837093.md`
