---
id: UDG@20.15.2@MMLCommand@DSP UPDIAMAAASTATUS
type: MMLCommand
name: DSP UPDIAMAAASTATUS（查询Diameter AAA服务器状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPDIAMAAASTATUS
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA服务器状态
status: active
---

# DSP UPDIAMAAASTATUS（查询Diameter AAA服务器状态）

## 功能

**适用NF：UPF**

该命令用来查询所有Diameter AAA服务器或者指定Diameter AAA服务器的连接状态。

## 注意事项

未查询到Diameter AAA服务器状态，说明此Diameter AAA未配置Diameter链路或未配置当前集中点模式对应的有效链路。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA服务器主机名称。<br>数据来源：本端规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT2670控制是否区分大小写。BIT2670值为0时，不区分大小写；值为1时，区分大小写，。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMAAASTATUS]] · Diameter AAA服务器状态（UPDIAMAAASTATUS）

## 使用实例

- 查询指定名字的Diameter AAA服务器的状态信息：
  ```
  %%DSP UPDIAMAAASTATUS: HOSTNAME="diamaaawgy1";
  ```
  ```
  %%
  RETCODE = 0 Operation Success.
  Diameter AAA服务器状态
  ----------------------
      主机名  =  diamaaawgy1
     POD名称  =  updiam-pod-0
    本端地址  =  10.135.21.18
  本端子地址  =  -
    对端地址  =  10.194.39.105
        状态  =  Abnormal
  本端主机名  =  zhgroup7
  本端端口号  =  19681
  对端端口号  =  3868
  (结果个数 = 1)
  --- END
  ```
- 查询所有已经配置的Diameter AAA服务器的主机名：
  ```
  %%DSP UPDIAMAAASTATUS:;
  ```
  ```
  %%
  RETCODE = 0  Operation Success.
  Diameter AAA服务器状态
  --------------------------
  主机名                  POD名称         本端地址         本端子地址       对端地址         状态        本端主机名    本端端口号   对端端口号
  154diam-aaa-swm-mao     updiam-pod-0    10.154.71.53     -                10.202.154.15    Abnormal    zhgroup7      19681        3868
  154diam-aaa-swm-mao     updiam-pod-0    10.154.71.53     -                10.202.154.14    Abnormal    zhgroup7      19681        3868
  154diam-aaa-swm-mao-s   updiam-pod-0    10.154.71.53     -                10.202.154.16    Abnormal    zhgroup7      19681        3868
  (结果个数= 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UPDIAMAAASTATUS.md`
