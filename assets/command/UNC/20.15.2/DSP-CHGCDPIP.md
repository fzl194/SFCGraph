---
id: UNC@20.15.2@MMLCommand@DSP CHGCDPIP
type: MMLCommand
name: DSP CHGCDPIP（显示计费相关的IP配置参数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CHGCDPIP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- CDPIP 配置
status: active
---

# DSP CHGCDPIP（显示计费相关的IP配置参数）

## 功能

**适用网元：SGSN**

该命令用于显示各RU使用的Ga接口本端地址。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要显示Ga接口本端地址的RU。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：0~63 位字符串<br>默认值：无 |

## 操作的配置对象

- [计费相关的IP配置参数（CHGCDPIP）](configobject/UNC/20.15.2/CHGCDPIP.md)

## 使用实例

显示Ga接口本端配置：

DSP CHGCDPIP:;

```
%%DSP CHGCDPIP:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
            RU名称  =  USN_SP_RU_0066
        IP地址类型  =  IPv4地址
          IPv4地址  =  192.168.26.1
            端口号  =  4026
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示计费相关的IP配置参数(DSP-CHGCDPIP)_26305176.md`
