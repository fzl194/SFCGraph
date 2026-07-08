---
id: UDG@20.15.2@MMLCommand@LST APNTETHERDETSW
type: MMLCommand
name: LST APNTETHERDETSW（查询APN Tethering终端数量检测开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNTETHERDETSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- APN Tethering用户终端数量检测开关配置
status: active
---

# LST APNTETHERDETSW（查询APN Tethering终端数量检测开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示APN下Tethering终端数量检测开关信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNTETHERDETSW]] · APN Tethering终端数量检测开关（APNTETHERDETSW）

## 使用实例

假如运营商查询名称为“huawei.com”的APN的Tethering的终端数量检测开关信息：

```
%%LST APNTETHERDETSW: APN="huawei.com";
```

```
%%
RETCODE = 0 操作成功。

APN Tethering终端数量检测开关
----------------------------------------------------------
     APN = huawei.com
开关标识 = 开启
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNTETHERDETSW.md`
