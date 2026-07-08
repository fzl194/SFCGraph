---
id: UNC@20.15.2@MMLCommand@DSP MVNOUSR
type: MMLCommand
name: DSP MVNOUSR（显示MVNO用户信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MVNOUSR
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
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO资源配置表
status: active
---

# DSP MVNOUSR（显示MVNO用户信息）

## 功能

**适用网元：SGSN、MME**

此命令用于查询MVNO的用户数和PDP上下文个数。

## 注意事项

- 如果输入“RUNAME”，就查询指定SPU资源单元上的当前MVNO用户个数和PDP上下文个数。如果没有输入“RUNAME”，则查询系统所有的MVNO的用户个数。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| MVNOID | MVNO标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO的标识ID。如果没有输入这个参数，则查询所有的MVNO的用户数。<br>取值范围：1~64<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MVNOUSR]] · MVNO用户信息（MVNOUSR）

## 使用实例

查询所有的MVNO的用户数：

DSP MVNOUSR:;

```
%%DSP MVNOUSR:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
        MVNO标识 =  2
    2G用户附着数 =  1
 2G用户激活PDP数 =  1
    3G用户附着数 =  2
 3G用户激活PDP数 =  3
    4G用户附着数 =  4
    4G建立承载数 =  5
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MVNOUSR.md`
