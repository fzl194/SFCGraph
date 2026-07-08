---
id: UNC@20.15.2@MMLCommand@LST GMMPTMSIREALLOC
type: MMLCommand
name: LST GMMPTMSIREALLOC（查询Gb模式PTMSI重分配控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GMMPTMSIREALLOC
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
- Gb模式PTMSI重分配控制参数
status: active
---

# LST GMMPTMSIREALLOC（查询Gb模式PTMSI重分配控制参数）

## 功能

**适用网元：SGSN**

此命令用于查询Gb模式PTMSI重分配控制参数。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GMMPTMSIREALLOC]] · Gb模式PTMSI重分配控制参数（GMMPTMSIREALLOC）

## 使用实例

查询Gb模式PTMSI重分配控制参数所有信息：

LST GMMPTMSIREALLOC:;

```
%%LST GMMPTMSIREALLOC:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                 伴随RAU流程分配  =  是
P-TMSI重分配流程间隔时长（小时）  =  0
        P-TMSI重分配流程发起条件  =  处于Ready状态
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GMMPTMSIREALLOC.md`
