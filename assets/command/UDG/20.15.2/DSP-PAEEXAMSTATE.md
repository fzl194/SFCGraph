---
id: UDG@20.15.2@MMLCommand@DSP PAEEXAMSTATE
type: MMLCommand
name: DSP PAEEXAMSTATE（显示PAE故障信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAEEXAMSTATE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 系统资源
status: active
---

# DSP PAEEXAMSTATE（显示PAE故障信息）

## 功能

该命令用于显示指定资源上的PAE内部故障情况。通过获取的信息，判断信息是否正常，以便故障定位。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [PAE故障信息（PAEEXAMSTATE）](configobject/UDG/20.15.2/PAEEXAMSTATE.md)

## 使用实例

显示所有资源PAE内部故障情况：

```
DSP PAEEXAMSTATE:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
微服务类型  微服务实例号  故障类型                  有故障    阈值（%）    当前值（%）    TP         

aa          aa            PAE线程死循环             否        NULL         NULL           0xFFFFFFFF 
aa          aa            共享队列过载              否        80           0              0x1001     
aa          aa            共享队列破坏              否        NULL         NULL           0xFFFFFFFF 
aa          aa            共享队列死锁              否        NULL         NULL           0xFFFFFFFF 
aa          aa            PAE私有队列过载           否        80           0              0xFFFFFFFF 
aa          aa            PAE私有队列破坏           否        NULL         NULL           0xFFFFFFFF 
aa          aa            PAE私有队列死锁           否        NULL         NULL           0xFFFFFFFF 
aa          aa            共享内存过载              否        80           0              0xFFFFFFFF 
aa          aa            共享内存破坏              否        NULL         NULL           0xFFFFFFFF 
aa          aa            共享内存泄露              否        50           0              0xFFFFFFFF 
aa          aa            PAE私有内存过载           否        NULL         NULL           0xFFFFFFFF 
aa          aa            PAE私有内存破坏           否        NULL         NULL           0xFFFFFFFF 
aa          aa            PAE私有内存泄露           否        50           0              0xFFFFFFFF 
aa          aa            Fabric所有平面不可达      否        NULL         NULL           0xFFFFFFFF 
aa          aa            外联口发送失败超限告警    否        1            0              0xFFFFFFFF 
aa          aa            内联口发送失败超限告警    否        1            0              0xFFFFFFFF 
aa          aa            TUN口发送失败超限告警     否        1            0              0xFFFFFFFF 
aa          aa            TAP口发送失败超限告警     否        1            0              0xFFFFFFFF 
aa          aa            共享内存耗尽告警          否        NULL         NULL           0xFFFFFFFF 
aa          aa            控制线程死循环            否        NULL         NULL           0xFFFFFFFF 
bb          bb            PAE线程死循环             否        NULL         NULL           0xFFFFFFFF 
bb          bb            共享队列过载              否        80           0              0x1001     
bb          bb            共享队列破坏              否        NULL         NULL           0xFFFFFFFF 
bb          bb            共享队列死锁              否        NULL         NULL           0xFFFFFFFF 
bb          bb            PAE私有队列过载           否        80           0              0xFFFFFFFF 
bb          bb            PAE私有队列破坏           否        NULL         NULL           0xFFFFFFFF 
bb          bb            PAE私有队列死锁           否        NULL         NULL           0xFFFFFFFF 
bb          bb            共享内存过载              否        80           0              0xFFFFFFFF 
bb          bb            共享内存破坏              否        NULL         NULL           0xFFFFFFFF 
bb          bb            共享内存泄露              否        50           0              0xFFFFFFFF 
bb          bb            PAE私有内存过载           否        NULL         NULL           0xFFFFFFFF 
bb          bb            PAE私有内存破坏           否        NULL         NULL           0xFFFFFFFF 
bb          bb            PAE私有内存泄露           否        50           0              0xFFFFFFFF 
bb          bb            Fabric所有平面不可达      否        NULL         NULL           0xFFFFFFFF 
bb          bb            外联口发送失败超限告警    否        1            0              0xFFFFFFFF 
bb          bb            内联口发送失败超限告警    否        1            0              0xFFFFFFFF 
bb          bb            TUN口发送失败超限告警     否        1            0              0xFFFFFFFF 
bb          bb            TAP口发送失败超限告警     否        1            0              0xFFFFFFFF 
bb          bb            共享内存耗尽告警          否        NULL         NULL           0xFFFFFFFF 
bb          bb            控制线程死循环            否        NULL         NULL           0xFFFFFFFF 
(结果个数 = 40)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE故障信息（DSP-PAEEXAMSTATE）_92520033.md`
