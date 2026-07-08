---
id: UNC@20.15.2@MMLCommand@DSP PAEBATCHRECVNUM
type: MMLCommand
name: DSP PAEBATCHRECVNUM（显示PAE批量接收报文数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEBATCHRECVNUM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 时延统计
status: active
---

# DSP PAEBATCHRECVNUM（显示PAE批量接收报文数）

## 功能

该命令用于显示PAE批量接收报文数。

## 注意事项

该命令查询到的为实际生效的批收数，若环境变量SVC_VFABRIC_FWD_BATCH_RECV_NUM与SET PAEBATCHRECVNUM配置同时存在时，MML配置优先生效；若无MML配置，查询结果为环境变量配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | Cell ID | 可选必选说明：可选参数<br>参数含义：该参数表示PAE调试消息发送的CELLID，可以通过使用<br>[**DSP PAENODE**](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)<br>命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [PAE批量接收报文数（PAEBATCHRECVNUM）](configobject/UNC/20.15.2/PAEBATCHRECVNUM.md)

## 使用实例

动态查询PAE批量收包数量：

```
+++    UNC/*MEID:0 MENAME:project-v6*/        2024-01-24 14:41:02
O&M    #174
%%DSP PAEBATCHRECVNUM:;%%
RETCODE = 0  操作成功

结果如下
--------
Cell ID  					PAE批收数量  

esa-pod-0__103__0				224          
csdb-pod-0__103__0				224          
ipapmexec-pod-b6988575-kmvm7__103__0		224   
isu-pod-1__103__0				224          
gcp-pod-1__103__0				224                                  
(结果个数 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAE批量接收报文数（DSP-PAEBATCHRECVNUM）_35145961.md`
