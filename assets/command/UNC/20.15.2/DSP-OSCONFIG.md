---
id: UNC@20.15.2@MMLCommand@DSP OSCONFIG
type: MMLCommand
name: DSP OSCONFIG（查询OS配置）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSCONFIG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- OS管理
status: active
---

# DSP OSCONFIG（查询OS配置）

## 功能

![](查询OS配置 (DSP OSCONFIG)_71313093.assets/notice_3.0-zh-cn_2.png)

执行重启，重建，扩容等涉及OS启动的动作后，立即查询相应节点网卡组播开关状态可能与预期配置不同，节点会在OS启动后30分钟内自动同步网卡组播开关配置。如需确认网卡组播开关状态，请30分钟后查询。

执行重启，重建，扩容等涉及OS启动的动作后，立即查询相应节点内存压缩状态可能与预期配置不同，节点会在OS启动后30分钟内自动同步内存压缩状态配置。如需确认内存压缩状态，请30分钟后查询。

执行重启，重建，扩容等涉及OS启动的动作后，立即查询相应节点DHE算法可能与预期配置不同，节点会在OS启动后30分钟内自动同步DHE算法配置。如需确认DHE算法配置，请30分钟后查询。

该命令用于查询OS配置。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 当环境出现网卡变更（例如：新增网卡、网卡故障、新增容器和容器重启等）的情况时，可能会使节点网卡组播状态不一致。建议再次执行[**SET OSCONFIG**](设置OS配置 (SET OSCONFIG)_23147326.md)命令开启/关闭网卡组播能力。
- 查询指定操作类型时，若某一节点状态异常导致查询失败，该节点的查询信息会显示NULL。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OPERATETYPE | 操作类型 | 可选必选说明：必选参数。<br>参数含义：用于查询OS配置的操作类型。<br>取值范围：<br>- “MULTICAST（组播）”：OS配置为组播类型。<br>- “MEMSWAP（内存压缩）”：OS配置为内存压缩类型。<br>- “DHEALGORITHM（DHE算法）”：OS配置为DHE算法类型。<br>默认值：无。<br>配置原则：无。 |
| MEID | 网元ID | 可选必选说明：当<br>“操作类型”<br>为<br>“MEMSWAP（内存压缩）”<br>时为条件可选参数。<br>参数含义：用于指示系统需要设置指定网元ID下的节点数据。“网元ID”可以通过执行<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md#ZH-CN_MMLREF_0000001147084797__mmlfunc13177628172748)<br>查询。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSCONFIG]] · OS配置（OSCONFIG）

## 使用实例

“操作类型” 为 “MULTICAST（组播）” 时， 结果以进度上报形式展示，此处只显示最终结果数据：

```
%%DSP OSCONFIG: OPERATETYPE=MULTICAST;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
节点IP    操作类型  状态  

10.0.0.0  组播      关闭     
10.0.0.0  组播      关闭     
10.0.0.0  组播      关闭     
10.0.0.0  组播      关闭     
(结果个数 = 4)

共有5个报告
---    END
```

“操作类型” 为 “MEMSWAP（内存压缩）” 时， 结果以进度上报形式展示，此处只显示最终结果数据：

```
%%DSP OSCONFIG: OPERATETYPE=MEMSWAP;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
网元ID  节点IP    虚拟机类型  开关 

0       10.0.0.0  CSP_B       关闭  
0       10.0.0.0  CSP_C       关闭
0       10.0.0.0  CSP_A       关闭   
(结果个数 = 3)

共有5个报告
---    END
```

“操作类型” 为 “DHEALGORITHM（DHE算法）” 时， 结果以进度上报形式展示，此处只显示最终结果数据：

```
%%DSP OSCONFIG: OPERATETYPE=DHEALGORITHM;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
节点IP       操作类型  DHE密钥长度    
10.0.0.1     DHE算法   3072          
10.0.0.2     DHE算法   3072          
10.0.0.3     DHE算法   3072          
10.0.0.4     DHE算法   3072          
(结果个数 = 4)  

共有5个报告 
---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSCONFIG.md`
