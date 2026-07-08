---
id: UNC@20.15.2@MMLCommand@DSP PLGPKGSTATE
type: MMLCommand
name: DSP PLGPKGSTATE（显示扩展包运行状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PLGPKGSTATE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 系统维护
- 业务扩展包管理
status: active
---

# DSP PLGPKGSTATE（显示扩展包运行状态）

## 功能

**适用网元：SGSN、MME**

该命令用于查询USN扩展包状态以及USN与其他VNFC网元扩展包状态同步结果。

## 注意事项

当前只实现与CSLB状态同步结果查询

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLGPKGSTATE]] · 扩展包运行状态（PLGPKGSTATE）

## 使用实例

显示扩展包运行状态：

DSP PLGPKGSTATE:;

```
RETCODE = 0  操作成功。

查询结果如下
------------------------
 USN_VNFC扩展包生效状态  =  生效
CSLB_VNFC扩展包生效状态  =  生效
                  同步时间  =   2015-11-19 14:18:46
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示扩展包运行状态(DSP-PLGPKGSTATE)_72345959.md`
