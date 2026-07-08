---
id: UDG@20.15.2@MMLCommand@LST IFFLOWALMTHD
type: MMLCommand
name: LST IFFLOWALMTHD（查询接口带宽利用率告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IFFLOWALMTHD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口带宽利用率告警阈值
status: active
---

# LST IFFLOWALMTHD（查询接口带宽利用率告警阈值）

## 功能

该命令用于查询接口带宽利用率告警阈值。

若不指定IFNAME参数时，则查询所有接口的带宽利用率告警阈值；若指定IFNAME参数时，则可以查询指定接口的带宽利用率告警阈值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定带宽利用率告警阈值的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [接口带宽利用率告警阈值（IFFLOWALMTHD）](configobject/UDG/20.15.2/IFFLOWALMTHD.md)

## 使用实例

查询接口带宽利用率阈值：

```
LST IFFLOWALMTHD:IFNAME="ethernet64/0/3";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                         接口名  =  Ethernet64/0/3
入向带宽利用率告警产生阈值（%）  =  100
入向带宽利用率告警恢复阈值（%）  =  100
出向带宽利用率告警产生阈值（%）  =  100
出向带宽利用率告警恢复阈值（%）  =  100

(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询接口带宽利用率告警阈值（LST-IFFLOWALMTHD）_00840873.md`
