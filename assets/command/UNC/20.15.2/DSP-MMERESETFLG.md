---
id: UNC@20.15.2@MMLCommand@DSP MMERESETFLG
type: MMLCommand
name: DSP MMERESETFLG（查询MME复位标志）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MMERESETFLG
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 系统参数管理
status: active
---

# DSP MMERESETFLG（查询MME复位标志）

## 功能

**适用网元：MME**

此命令用于查看MME复位标志。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMERESETFLG]] · MME复位标志（MMERESETFLG）

## 使用实例

查询MME复位标志：

DSP MMERESETFLG:;

```
%%DSP MMERESETFLG:;%%
RETCODE = 0  操作成功

输出结果如下：
-------------------------
MME复位标志  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MMERESETFLG.md`
