---
id: UNC@20.15.2@MMLCommand@LST PMMPTMSIREALLOC
type: MMLCommand
name: LST PMMPTMSIREALLOC（查询Iu模式PTMSI重分配控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PMMPTMSIREALLOC
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM流程管理
- Iu模式PTMSI重分配控制参数
status: active
---

# LST PMMPTMSIREALLOC（查询Iu模式PTMSI重分配控制参数）

## 功能

**适用网元：SGSN**

此命令用于查询Iu模式PTMSI重分配控制参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PMMPTMSIREALLOC]] · Iu模式PTMSI重分配控制参数（PMMPTMSIREALLOC）

## 使用实例

查询Iu模式PTMSI重分配控制参数所有信息：

LST PMMPTMSIREALLOC:;

```
%%LST PMMPTMSIREALLOC:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                 伴随RAU流程分配  =  否
P-TMSI重分配流程间隔时长（小时）  =  1
        P-TMSI重分配流程发起条件  =  PTMSI分配后
(结果个数 = 1)

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Iu模式PTMSI重分配控制参数(LST-PMMPTMSIREALLOC)_26145522.md`
