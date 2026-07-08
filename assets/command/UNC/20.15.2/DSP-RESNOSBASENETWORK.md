---
id: UNC@20.15.2@MMLCommand@DSP RESNOSBASENETWORK
type: MMLCommand
name: DSP RESNOSBASENETWORK（查询NOS Base平面网络信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RESNOSBASENETWORK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- 资源实例管理
status: active
---

# DSP RESNOSBASENETWORK（查询NOS Base平面网络信息）

## 功能

该命令用于查询NOS Base平面网络信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESOURCE | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：请使用<br>[**DSP RES**](显示资源信息（DSP RES）_59036939.md)<br>查看资源名称。 |

## 操作的配置对象

- [NOS Base平面网络信息（RESNOSBASENETWORK）](configobject/UNC/20.15.2/RESNOSBASENETWORK.md)

## 使用实例

查询 “资源名称” 为 “OMU1” 的NOS Base平面网络信息：

```
DSP RESNOSBASENETWORK: RESOURCE="OMU1";
```

```
RETCODE = 0  操作成功

结果如下
---------
       资源名称  =  OMU1
VNF外部组网类型  =  三层组网
VNF内部网络类型  =  Bridge
   Base平面数目  =  1
   Base通道数目  =  1
Base IP地址来源  =  系统内部分配
  Base IP版本号  =  IPv4
       绑定模式  =  -
    绑定MAC模式  =  -
   绑定成员数目  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NOS-Base平面网络信息（DSP-RESNOSBASENETWORK）_15247350.md`
