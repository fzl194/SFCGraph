---
id: UNC@20.15.2@MMLCommand@SET OSCONFIG
type: MMLCommand
name: SET OSCONFIG（设置OS配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OSCONFIG
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 设备管理
- OS管理
status: active
---

# SET OSCONFIG（设置OS配置）

## 功能

![](设置OS配置 (SET OSCONFIG)_23147326.assets/notice_3.0-zh-cn_2.png)

该命令为高危命令，此命令将修改节点配置，会造成部分业务暂时不可用，请务必在华为技术支持人员的指导下使用该命令。

如果执行该命令，当命令的 “操作类型” 选择 “MULTICAST（组播）” 时，节点会在OS启动30分钟内自动同步网卡组播开关配置。

如果执行该命令，当命令的 “操作类型” 选择 “MEMSWAP（内存压缩）” 时，节点会在OS启动5分钟内自动同步内存压缩开关配置，并需要等待一段时间才能完成内存压缩。多次打开内存压缩开关，由于内存压缩率不同，内存使用存在少量波动。

如果执行该命令，当命令的 “操作类型” 选择 “DHEALGORITHM（DHE算法）” 时，节点会在OS启动10分钟内自动同步DHE密钥长度配置。

该命令用于设置OS配置。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

环境处于升级、回退、补丁、观察期或备份状态，禁止执行该命令。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OPERATETYPE | 操作类型 | 可选必选说明：必选参数。<br>参数含义：用于设置OS配置的操作类型。<br>取值范围：<br>- “MULTICAST（组播）”：OS配置为组播类型。<br>- “MEMSWAP（内存压缩）”：OS配置为内存压缩类型。<br>- “DHEALGORITHM（DHE算法）”：OS配置为DHE算法类型。<br>默认值：无。<br>配置原则：无。 |
| SWITCH | 开关 | 可选必选说明：当<br>“操作类型”<br>为<br>“MULTICAST（组播）”<br>或<br>“MEMSWAP（内存压缩）”<br>时为条件必选参数。<br>参数含义：用于设置网卡组播开关（不包括lo、veth和gre0网卡），内存压缩开关。<br>取值范围：<br>- “ON（开启）”<br>：网卡组播/内存压缩类型为开。<br>- “OFF（关闭）”：网卡组播/内存压缩类型为关。<br>默认值：无。<br>配置原则：无。 |
| MEID | 网元ID | 可选必选说明：当<br>“操作类型”<br>为<br>“MEMSWAP（内存压缩）”<br>时为条件必选参数。<br>参数含义：用于指示系统需要设置指定网元ID下的节点数据。“网元ID”可以通过执行<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md#ZH-CN_MMLREF_0000001147084797__mmlfunc13177628172748)<br>查询。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| VDUTYPE | 虚拟机类型 | 可选必选说明：当<br>“操作类型”<br>为<br>“MEMSWAP（内存压缩）”<br>时为条件必选参数。<br>参数含义：用于指示系统需要设置指定虚拟机类型下的节点数据。“虚拟机类型”可以通过执行<br>[**DSP NODE**](../节点管理/节点查询（DSP NODE）_71678755.md#ZH-CN_TOPIC_0171678755__section165251150144313)<br>查询。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：无。 |
| KEYLENGTH | DHE密钥长度 | 可选必选说明：当<br>“操作类型”<br>为<br>“DHEALGORITHM（DHE算法）”<br>时为条件必选参数。<br>参数含义：用于设置SSHD服务的DHE算法的密钥长度。<br>取值范围：<br>- “2048（2048）”<br>：SSHD服务的DHE算法密钥长度最小长度为2048。<br>- “3072（3072）”：SSHD服务的DHE算法密钥长度最小长度为3072。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [OS配置（OSCONFIG）](configobject/UNC/20.15.2/OSCONFIG.md)

## 使用实例

设置 “操作类型” 为 “MULTICAST（组播）” ， “开关” 为 “ON” 时，结果以进度上报形式展示，此处只显示最终结果数据：

```
%%SET OSCONFIG: OPERATETYPE=MULTICAST, SWITCH=ON;%%
RETCODE = 0  操作成功

共有5个报告
---    END
```

设置 “操作类型” 为 “MEMSWAP（内存压缩）” ， “开关” 为 “ON” 时，结果以进度上报形式展示，此处只显示最终结果数据：

```
%%SET OSCONFIG: OPERATETYPE=MEMSWAP, MEID=0, VDUTYPE="CSP_B", SWITCH=ON;%%
RETCODE = 0  操作成功

操作结果如下
------------
     网元ID  =  0
     节点IP  =  10.0.0.0
 虚拟机类型  =  CSP_B
   操作状态  =  成功
 (结果个数 = 1)

共有5个报告
---    END
```

设置 “操作类型” 为 “DHEALGORITHM（DHE算法）” ， “DHE密钥长度” 为 “3072” 时，结果以进度上报形式展示，此处只显示最终结果数据：

```
%%SET OSCONFIG: OPERATETYPE=DHEALGORITHM, KEYLENGTH=3072;%% 
RETCODE = 0  操作成功 

操作结果如下 
------------ 
节点IP       操作类型  详细信息    
10.0.0.1     DHE算法   操作成功   
10.0.0.2     DHE算法   操作成功  
10.0.0.3     DHE算法   操作成功   
10.0.0.4     DHE算法   操作成功  
 (结果个数 = 4)  
共有5个报告 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置OS配置-(SET-OSCONFIG)_23147326.md`
