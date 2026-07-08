---
id: UNC@20.15.2@MMLCommand@DSP USRCTLGGSN
type: MMLCommand
name: DSP USRCTLGGSN（显示手工恢复GGSN地址状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: USRCTLGGSN
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GGSN容灾功能
status: active
---

# DSP USRCTLGGSN（显示手工恢复GGSN地址状态）

## 功能

**适用网元：SGSN**

此命令用于查询需要手工恢复的GGSN地址。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRCTLGGSN]] · 手工恢复GGSN地址（USRCTLGGSN）

## 使用实例

1. 查询所有需要手工恢复的GGSN地址： DSP USRCTLGGSN:;
  ```
  %%DSP USRCTLGGSN:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   IP地址类型  本端IP地址     对端IP地址 

   IPv4        192.168.14.20  192.168.45.20
   IPv4        192.168.14.20  192.168.45.21
   IPv4        192.168.14.20  192.168.45.23
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示手工恢复GGSN地址状态(DSP-USRCTLGGSN)_26305716.md`
