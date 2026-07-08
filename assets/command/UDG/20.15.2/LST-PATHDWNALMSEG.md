---
id: UDG@20.15.2@MMLCommand@LST PATHDWNALMSEG
type: MMLCommand
name: LST PATHDWNALMSEG（查询单条路径断告警抑制参数的分段配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PATHDWNALMSEG
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 单条路径断告警的分段抑制参数
status: active
---

# LST PATHDWNALMSEG（查询单条路径断告警抑制参数的分段配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询指定eNodeB/gNodeB地址段内的单条路径断告警抑制的配置：

需要输入IP地址版本以及eNodeB/gNodeB的起始和中止地址进行查询。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBIPVERSION | IP地址版本 | 可选必选说明：可选参数<br>参数含义：该参数用于设置地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| V4STARTIP | IPv4类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V4ENDIP | IPv4类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V6STARTIP | IPv6类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| V6ENDIP | IPv6类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [单条路径断告警抑制参数的分段配置（PATHDWNALMSEG）](configobject/UDG/20.15.2/PATHDWNALMSEG.md)

## 使用实例

查询单条路径断告警抑制参数的分段配置：

```
LST PATHDWNALMSEG:;
```

```

RETCODE = 0  操作成功。

单路径告警抑制参数分段配置
--------------------------
        告警上报的连续中断次数  =  5
            告警上报的探测次数  =  5
        告警上报的累计中断次数  =  5
        告警恢复的连续正常次数  =  5
                            IP地址类型  = IPV4
IPv4类型的eNodeB地址段起始地址  =  10.1.1.1
IPv4类型的eNodeB地址段终止地址  =  10.1.1.10
IPv6类型的eNodeB地址段起始地址  =  ::
IPv6类型的eNodeB地址段终止地址  =  ::
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询单条路径断告警抑制参数的分段配置（LST-PATHDWNALMSEG）_82837866.md`
