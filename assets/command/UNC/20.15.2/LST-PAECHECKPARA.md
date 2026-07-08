---
id: UNC@20.15.2@MMLCommand@LST PAECHECKPARA
type: MMLCommand
name: LST PAECHECKPARA（查询PAE寻呼反压流控检测参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PAECHECKPARA
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

# LST PAECHECKPARA（查询PAE寻呼反压流控检测参数）

## 功能

**适用NF：MME、AMF**

该命令用于查询LINK节点相关资源过载检测参数，包括link-pod内pBuf资源和PAE与虚拟交换机间消息发送队列所使用的检测周期、检测次数等信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PAECHECKPARA]] · PAE寻呼反压流控检测参数（PAECHECKPARA）

## 使用实例

查询PAE寻呼反压流控检测参数：

```
%%LST PAECHECKPARA:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------ 
检测间隔（s）  =  1
检测次数       =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PAECHECKPARA.md`
