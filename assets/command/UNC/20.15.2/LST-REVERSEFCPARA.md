---
id: UNC@20.15.2@MMLCommand@LST REVERSEFCPARA
type: MMLCommand
name: LST REVERSEFCPARA（查询PAE寻呼反压流控启动/恢复阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: REVERSEFCPARA
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

# LST REVERSEFCPARA（查询PAE寻呼反压流控启动/恢复阈值）

## 功能

**适用NF：MME、AMF**

该命令用于查询系统反压流控检测门限参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/REVERSEFCPARA]] · PAE寻呼反压流控启动/恢复阈值（REVERSEFCPARA）

## 使用实例

查询PAE寻呼反压流控启动/恢复阈值：

```
%%LST REVERSEFCPARA:;%%
RETCODE = 0  操作成功

操作结果如下
------------------------ 
      控制策略  =  百分比
 过载阈值（%）  =  50
 恢复阈值（%）  =  5
过载阈值（个）  =  1
恢复阈值（个）  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-REVERSEFCPARA.md`
