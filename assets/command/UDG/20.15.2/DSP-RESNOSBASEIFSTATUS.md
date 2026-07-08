---
id: UDG@20.15.2@MMLCommand@DSP RESNOSBASEIFSTATUS
type: MMLCommand
name: DSP RESNOSBASEIFSTATUS（查询NOS Base平面网络的网口状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESNOSBASEIFSTATUS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 系统调测
- 基础网络调测
status: active
---

# DSP RESNOSBASEIFSTATUS（查询NOS Base平面网络的网口状态信息）

## 功能

该命令用于查询NOS Base平面网络的网口状态及IP信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源名称或容器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的资源的信息。使用<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>查看资源名称。 |

## 操作的配置对象

- [NOS Base平面网络的网口状态信息（RESNOSBASEIFSTATUS）](configobject/UDG/20.15.2/RESNOSBASEIFSTATUS.md)

## 使用实例

- 查询所有资源的NOS Base网口状态及IP信息：
  ```
  DSP RESNOSBASEIFSTATUS:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  资源名称  接口名称  接口状态  接口IPv4地址  接口IPv6地址

  OMU1      eth1      UP        NULL          fc00:f111:2222:3333:4444:5555:2111:1d8
  OMU2      eth1      UP        NULL          fc00:f111:2222:3333:4444:5555:2111:206
  (结果个数 = 2)

  ---    END
  ```

- 查询“资源名称”为“OMU1”的NOS Base网口状态及IP信息：
  ```
  DSP RESNOSBASEIFSTATUS: RESNAME="OMU1";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
      资源名称  =  OMU1
      接口名称  =  eth1
      接口状态  =  UP
  接口IPv4地址  =  NULL
  接口IPv6地址  =  fc00:f111:2222:3333:4444:5555:2111:1d8
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NOS-Base平面网络的网口状态信息（DSP-RESNOSBASEIFSTATUS）_00404596.md`
