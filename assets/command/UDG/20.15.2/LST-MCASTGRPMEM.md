---
id: UDG@20.15.2@MMLCommand@LST MCASTGRPMEM
type: MMLCommand
name: LST MCASTGRPMEM（查询组播组成员配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MCASTGRPMEM
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 组播组成员配置
status: active
---

# LST MCASTGRPMEM（查询组播组成员配置）

## 功能

**适用NF：UPF**

该命令用于查询静态组播组IMSI成员记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [组播组成员配置（MCASTGRPMEM）](configobject/UDG/20.15.2/MCASTGRPMEM.md)

## 使用实例

查询静态组播组成员配置：

```
LST MCASTGRPMEM:;
```

```

RETCODE = 0  操作成功

结果如下
--------
组播组名称  成员类型  IMSI            VXLAN隧道端点名称  双发选收结对ID

MtcstGrp1   IMSI      18456789012342  null               0
MtcstGrp1   IMSI      18456789012353  null               0
MtcstGrp1   IMSI      18456789012359  null               0
group       IMSI      1234567748      null               0
group       IMSI      123456778       null               0
group       VTEP      null            vtep1              0
(结果个数 = 6)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询组播组成员配置（LST-MCASTGRPMEM）_15470553.md`
