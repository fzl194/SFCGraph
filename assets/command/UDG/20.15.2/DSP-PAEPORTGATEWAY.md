---
id: UDG@20.15.2@MMLCommand@DSP PAEPORTGATEWAY
type: MMLCommand
name: DSP PAEPORTGATEWAY（显示PAE端口网关信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAEPORTGATEWAY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 端口
status: active
---

# DSP PAEPORTGATEWAY（显示PAE端口网关信息）

## 功能

该命令用于显示指定资源上PAE端口对应的网关信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。仅支持数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符。<br>默认值：无<br>配置原则：<br>使用DSP PAENODE查看“工作角色”为“数据转发”的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于标识微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。仅支持数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符。<br>默认值：无<br>配置原则：<br>使用DSP PAENODE查看“工作角色”为“数据转发”的微服务实例号。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAEPORTGATEWAY]] · PAE端口网关信息（PAEPORTGATEWAY）

## 使用实例

显示PAE端口的网关信息：

```
%%DSP PAEPORTGATEWAY:;%%
RETCODE = 0  操作成功

结果如下
--------
微服务类型  微服务实例号                            网段索引  平面ID  端口名称  端口类型  网关IP地址        网关MAC地址       端口状态

104         comtest-pod-0172-16-1-146__103__0       1         0       uio1      内联口    192.168.131.1     0427-5855-7231    up           
104         comtest-pod-0172-16-1-146__103__0       2         1       uio3      内联口    192.168.132.1     0427-5855-7232    up           
104         csdb-pod-0172-16-1-100__103__0          1         0       uio0      内联口    192.168.131.1     0427-5855-7231    up           
104         csdb-pod-0172-16-1-100__103__0          2         1       uio1      内联口    192.168.132.1     0427-5855-7232    up
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE端口网关信息（DSP-PAEPORTGATEWAY）_48803866.md`
