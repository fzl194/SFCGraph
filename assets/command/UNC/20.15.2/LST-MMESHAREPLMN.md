---
id: UNC@20.15.2@MMLCommand@LST MMESHAREPLMN
type: MMLCommand
name: LST MMESHAREPLMN（查询MME的共享PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMESHAREPLMN
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME POOL区管理
- MME共享管理
status: active
---

# LST MMESHAREPLMN（查询MME的共享PLMN）

## 功能

**适用网元：MME**

此命令用于查看MME的共享PLMN。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMESHAREPLMN]] · MME的共享PLMN（MMESHAREPLMN）

## 使用实例

查看MME的共享PLMN：

LST MMESHAREPLMN:;

```
%%LST MMESHAREPLMN:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
移动国家码  =  123
  移动网号  =  01
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MMESHAREPLMN.md`
