---
id: UNC@20.15.2@MMLCommand@LST PAECHECKTHD
type: MMLCommand
name: LST PAECHECKTHD（查询PAE寻呼反压流控检测阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PAECHECKTHD
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- PAE寻呼反压流控管理
status: active
---

# LST PAECHECKTHD（查询PAE寻呼反压流控检测阈值）

## 功能

**适用NF：MME、AMF**

该命令用于查询LINK节点相关资源过载检测阈值参数，包括link-pod内pBuf资源使用率过载、恢复门限，PAE与虚拟交换机间消息发送队列使用率过载、恢复门限等信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示检测的资源类型。<br>数据来源：本端规划<br>取值范围：<br>- PBUF（link-pod内使用的pBuf资源）<br>- SHAREQUEUE（PAE与软SDN间消息发送队列）<br>默认值：无<br>配置原则： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAECHECKTHD]] · PAE寻呼反压流控检测阈值（PAECHECKTHD）

## 使用实例

查询PAE寻呼反压流控检测阈值：

```
%%LST PAECHECKTHD:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------ 
资源类型                              触发过载阈值（%）    触发过载恢复阈值（%）    
link-pod内使用的pBuf资源              80                   50                       
PAE与软SDN间消息发送队列              80                   50                       
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PAE寻呼反压流控检测阈值(LST-PAECHECKTHD)_13911930.md`
