---
id: UNC@20.15.2@MMLCommand@LST SGWCHGPAUSE
type: MMLCommand
name: LST SGWCHGPAUSE（查询SGW的计费暂停功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWCHGPAUSE
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 计费暂停管理
- SGW计费暂停管理
status: active
---

# LST SGWCHGPAUSE（查询SGW的计费暂停功能）

## 功能

**适用NF：SGW-C**

该命令用于查询SGW计费暂停功能的参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWCHGPAUSE]] · SGW的计费暂停功能（SGWCHGPAUSE）

## 使用实例

查询SGW中计费暂停功能参数配置：

```
%%LST SGWCHGPAUSE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
 S1 Release触发计费暂停开关  =  DISABLE
 DDN寻呼失败触发计费暂停开关  =  DISABLE
下行报文阈值触发计费暂停开关  =  DISABLE
               下行报文阈值  =  500
  计费暂停时下行报文处理动作  =  buffer
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGW的计费暂停功能（LST-SGWCHGPAUSE）_89078989.md`
