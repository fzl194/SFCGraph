---
id: UNC@20.15.2@MMLCommand@DSP IULOAD
type: MMLCommand
name: DSP IULOAD（显示用户Iu连接负荷状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IULOAD
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu负荷配置
status: active
---

# DSP IULOAD（显示用户Iu连接负荷状态）

## 功能

**适用网元：SGSN**

该命令用于查询用户Iu连接负荷状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63 位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IULOAD]] · 用户Iu连接负荷状态（IULOAD）

## 使用实例

查询用户Iu连接负荷状态：

DSP IULOAD: RUNAME="USN_SP_RU_0064";

```
%%DSP IULOAD: RUNAME="USN_SP_RU_0064";%%
RETCODE = 0  操作成功。

查找IU负荷配置表
----------------
RU名称            进程号    负荷状态    连接数

USN_SP_RU_0064    0         正常        0     
USN_SP_RU_0064    1         正常        0     
USN_SP_RU_0064    2         正常        0     
USN_SP_RU_0064    3         正常        0     
USN_SP_RU_0064    4         正常        0     
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示用户Iu连接负荷状态(DSP-IULOAD)_26146038.md`
