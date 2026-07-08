---
id: UDG@20.15.2@MMLCommand@DSP ARPTABLE
type: MMLCommand
name: DSP ARPTABLE（显示ARP表项）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ARPTABLE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP表项统计查询
status: active
---

# DSP ARPTABLE（显示ARP表项）

## 功能

该命令用于显示接口上或设备上的所有ARP表项信息。查询条件组合如下：通过接口查询，通过VPN实例名称查询，通过RU名称查询，通过VPN实例名称+RU名称查询。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP表项的VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，取值范围是1～31。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置表项接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：查询指定资源单元的ARP表项。通过DSP RU命令可以查询资源单元信息。如果名称中包含空格则非法。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPTABLE]] · ARP表项（ARPTABLE）

## 使用实例

显示所有ARP表项：

```
DSP ARPTABLE:;
```

```

RETCODE = 0  操作成功

结果如下
--------
             IP地址  =  10.17.0.2
            MAC地址  =  00E0-FC12-3456
表项老化时间（min）  =  --
           表项类型  =  接口表项
        VPN实例名称  =  __mpp_vpn_inner__
           接口名称  =  GigabitEthernet0/0/1
             RU名称  =  VNODE_VNRS_VNFC_MAIN_0001
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-ARPTABLE.md`
