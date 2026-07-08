---
id: UDG@20.15.2@MMLCommand@LOD UPDIAMDICT
type: MMLCommand
name: LOD UPDIAMDICT（加载Diameter字典）
nf: UDG
version: 20.15.2
verb: LOD
object_keyword: UPDIAMDICT
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter字典管理
- 加载字典
status: active
---

# LOD UPDIAMDICT（加载Diameter字典）

## 功能

**适用NF：UPF**

![](加载Diameter字典（LOD UPDIAMDICT）_97314553.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，加载Diameter字典可能会导致UPF各Diameter应用对外接口呈现的变化，此时一般需要对端网元做同步的升级适配，否则可能造成业务异常。

该命令用于加载Diameter字典文件。

## 注意事项

- 该命令执行后立即生效。
- 可以通过ADD UPDIAMDICTPATH/MOD UPDIAMDICTPATH命令设置字典加载路径，通过LST UPDIAMDICTPATH命令查询字典加载路径。
- 执行命令前请确保对应目录下保存了Diameter控制文件，如果控制文件不齐全会导致字典加载失败。
- 该命令执行后UPF需要一段时间检查及同步字典文件数据。请在命令执行成功10-20s后，使用DSP UPDIAMDICTSTAT命令查看UPF当前加载字典路径是否修改。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DICTFILESELECT | 字典文件选择 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter字典类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：全部。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMDICT]] · Diameter字典（UPDIAMDICT）

## 使用实例

配置UPF的Swm应用使用用户定制的第一套Diameter字典文件：

```
MOD UPDIAMDICTPATH: APPLICATION=SWM,DICTNO=1,DICTPATH=CUSTOM1;
LOD UPDIAMDICT:DICTFILESELECT=ALL;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LOD-UPDIAMDICT.md`
