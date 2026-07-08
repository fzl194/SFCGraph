---
id: UNC@20.15.2@MMLCommand@DSP GBMSCONTNUM
type: MMLCommand
name: DSP GBMSCONTNUM（显示MS上下文数目和PDP上下文数目）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GBMSCONTNUM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- MS上下文管理
- 基本MS上下文管理
status: active
---

# DSP GBMSCONTNUM（显示MS上下文数目和PDP上下文数目）

## 功能

**适用网元：SGSN**

该命令用于查询指定GBP进程上MS上下文数目和PDP上下文数目。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置需要查询的GBP进程的进程号。<br>取值范围：0~20<br>默认值：无 |

## 操作的配置对象

- [MS上下文数目和PDP上下文数目（GBMSCONTNUM）](configobject/UNC/20.15.2/GBMSCONTNUM.md)

## 使用实例

查询USN_SP_RU_0064 1号进程上的GBP进程上的MS上下文和PDP上下文数据：

DSP GBMSCONTNUM: RUNAME="USN_SP_RU_0064", PN=1;

```
%%DSP GBMSCONTNUM: RUNAME="USN_SP_RU_0064", PN=1;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
                 RU名称  =  USN_SP_RU_0064
                 进程号  =  1
          MS 上下文个数  =  0
       BSSGP 上下文个数  =  0
         PDP 上下文个数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MS上下文数目和PDP上下文数目(DSP-GBMSCONTNUM)_26146020.md`
