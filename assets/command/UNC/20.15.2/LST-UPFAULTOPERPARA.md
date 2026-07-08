---
id: UNC@20.15.2@MMLCommand@LST UPFAULTOPERPARA
type: MMLCommand
name: LST UPFAULTOPERPARA（显示UP故障处理系统参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFAULTOPERPARA
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 辅锚点故障迁移
status: active
---

# LST UPFAULTOPERPARA（显示UP故障处理系统参数）

## 功能

**适用NF：SMF**

该命令用于显示UP故障处理的系统参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFAULTOPERPARA]] · UP故障处理系统参数（UPFAULTOPERPARA）

## 使用实例

查询UP故障处理的系统参数： LST UPFAULTOPERPARA:;

```
%%LST UPFAULTOPERPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
故障迁移速率(个/秒)  =  1000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPFAULTOPERPARA.md`
