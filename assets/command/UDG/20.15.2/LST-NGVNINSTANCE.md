---
id: UDG@20.15.2@MMLCommand@LST NGVNINSTANCE
type: MMLCommand
name: LST NGVNINSTANCE（查看5G VNInstance的配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGVNINSTANCE
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN基础配置
- 5G LAN实例配置
status: active
---

# LST NGVNINSTANCE（查看5G VNInstance的配置）

## 功能

**适用NF：UPF**

该命令用来查询已配置所有的5G LAN会话实例的配置信息。

## 注意事项

当PDN类型为IP时，MAC地址空闲时长开关、MAC地址空闲时长、IGMP Snooping开关、IGMP消息解析开关、组播转广播开关、广播流控开关、广播数据处理速率均为无效参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGVNINSTANCE]] · 5G VNInstance配置（NGVNINSTANCE）

## 使用实例

显示所有5G LAN会话实例配置：

```
%%LST NGVNINSTANCE:;
```

```
%%
RETCODE = 0  操作成功

VNInstance信息
--------------
               5G LAN组名称  =  a0000001-460-003-01
                       锁定  =  不使能
          IGMP Snooping开关  =  不使能
               组播泛洪开关  =  不使能
           IGMP消息解析开关  =  不使能
N3学习的MAC地址空闲时长开关  =  不使能
               报文检测方向  =  上行和下行报文
    N3学习的MAC地址空闲时长  =  60
                    PDN类型  =  Ethernet
               广播流控开关  =  不使能
           广播数据处理速率  =  0
               组播泛洪速率  =  0
               广播功能开关  =  不使能
                 精简组指示  =  否
        N6侧MAC地址空闲时长  =  60
               单播泛洪速率  =  0
N6学习的MAC地址空闲时长开关  =  不使能
               单播泛洪开关  =  不使能
               PDN连接类型  =  Vxlan隧道连接
        UPF间Vxlan隧道互通  =  是
                  VLAN类型  =  NULL
                  VLAN ID  =  0
      上行未知单播转N6/N19  =  使能
      上行未知组播转N6/N19  =  使能
         上行广播转N6/N19  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查看5G-VNInstance的配置（LST-NGVNINSTANCE）_12516585.md`
