---
id: UNC@20.15.2@MMLCommand@LST ADDRS1TACID
type: MMLCommand
name: LST ADDRS1TACID（查询S1TAC组内S1TAC号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRS1TACID
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配S1TAC段
status: active
---

# LST ADDRS1TACID（查询S1TAC组内S1TAC号段）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来查询指定S1TAC号段与S1TAC组的绑定关系或者配置的所有S1TAC号段和S1TAC组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | S1TAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRTACGROUP命令配置生成。 |
| TACSECNUM | S1TAC段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [S1TAC组内S1TAC号段（ADDRS1TACID）](configobject/UNC/20.15.2/ADDRS1TACID.md)

## 使用实例

查询指定S1TAC号段与S1TAC组的绑定关系：S1TAC组为wz-xs，S1TAC号段为2：

```
LST ADDRS1TACID: TACGROUPNAME="wz-xs", TACSECNUM=2;
RETCODE = 0  操作成功。

结果如下
------------------------
  S1TAC组名  =  wz-xs
S1TAC段编号  =  2
S1TAC起始ID  =  0x1
S1TAC终止ID  =  0x1F
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1TAC组内S1TAC号段（LST-ADDRS1TACID）_49644915.md`
