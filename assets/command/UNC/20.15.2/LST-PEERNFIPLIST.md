---
id: UNC@20.15.2@MMLCommand@LST PEERNFIPLIST
type: MMLCommand
name: LST PEERNFIPLIST（查询对端局向连接列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PEERNFIPLIST
command_category: 查询类
applicable_nf:
- AMF
- SMF
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST PEERNFIPLIST（查询对端局向连接列表）

## 功能

**适用NF：AMF、SMF、SMSF**

本命令用于查询对端局向连接列表，此局向连接列表用于与北向网管的对接，以及相关性能统计功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | 对端局向NF实例号 | 可选必选说明：可选参数<br>参数含义：对端局向NF实例号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| LOCALIP | 本端IP地址 | 可选必选说明：可选参数<br>参数含义：本端IP地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| PEERIP | 对端IP地址 | 可选必选说明：可选参数<br>参数含义：对端IP地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [对端局向连接列表（PEERNFIPLIST）](configobject/UNC/20.15.2/PEERNFIPLIST.md)

## 使用实例

若运营商想查询配置的对端局向连接列表，可用如下命令： LST PEERNFIPLIST:;

```
%%LST PEERNFIPLIST:;%%
RETCODE = 0  操作成功。

结果如下
------------------------ 
对端局向NF实例号  =  bf33a517-7789-4637-b675-b3591b0d706b
      本端IP地址  =  10.20.3.4
      对端IP地址  =  10.20.3.5
            掩码  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对端局向连接列表（LST-PEERNFIPLIST）_09653297.md`
