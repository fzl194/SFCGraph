---
id: UNC@20.15.2@MMLCommand@DSP CHGCDR
type: MMLCommand
name: DSP CHGCDR（显示强制生成用户话单的结果信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CHGCDR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费控制
status: active
---

# DSP CHGCDR（显示强制生成用户话单的结果信息）

## 功能

**适用网元：SGSN**

该命令用于查询执行 [**CRE CHGCDR**](强制生成用户话单（CRE CHGCDR）_26145374.md) 之后的结果信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令须在用[**CRE CHGCDR**](强制生成用户话单（CRE CHGCDR）_26145374.md)强制生成所有用户的话单之后使用。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDR | 话单类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要查询的话单类型。<br>取值范围：<br>- “S_CDR（S_CDR）”<br>- “M_CDR（M_CDR）”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCDR]] · 强制生成用户话单（CHGCDR）

## 使用实例

查询强制生成所有用户的M-CDR话单之后的结果信息：

DSP CHGCDR: CDR=M_CDR;

```
%%DSP CHGCDR: CDR=M_CDR;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
RU名称                进程号        进程类型        时间戳                     成功的话单数目        失败的话单数目 
USN_SP_RU_0066        0             SPP             2015-11-19 14:18:46        1                     0           
USN_SP_RU_0067        0             SPP             2015-11-19 14:18:46        0                     0           
USN_SP_RU_0067        1             SPP             2015-11-19 14:18:46        0                     0           
USN_SP_RU_0066        1             SPP             2015-11-19 14:18:46        0                     0        
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CHGCDR.md`
