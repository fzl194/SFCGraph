---
id: UNC@20.15.2@MMLCommand@DSP DNSDYNAMICIPV6HOST
type: MMLCommand
name: DSP DNSDYNAMICIPV6HOST（查询DNS IPv6动态域名）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DNSDYNAMICIPV6HOST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 域名管理
- DNS IPv6动态域名
status: active
---

# DSP DNSDYNAMICIPV6HOST（查询DNS IPv6动态域名）

## 功能

该命令用于显示DNS IPv6动态域名。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOST | DNS域名 | 可选必选说明：可选参数<br>参数含义：该参数用于显示DNS IPv6动态域名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSDYNAMICIPV6HOST]] · DNS IPv6动态域名（DNSDYNAMICIPV6HOST）

## 使用实例

显示IPv6动态域名：

```
DSP DNSDYNAMICIPV6HOST:;
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
            DNS域名  =  huawei.com
           IPv6地址  =  2001:DB8::11
      老化时间（s）  =  544
        (结果个数 = 1)

        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DNSDYNAMICIPV6HOST.md`
