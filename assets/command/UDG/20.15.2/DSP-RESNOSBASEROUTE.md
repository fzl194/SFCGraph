---
id: UDG@20.15.2@MMLCommand@DSP RESNOSBASEROUTE
type: MMLCommand
name: DSP RESNOSBASEROUTE（查询NOS Base平面网络的路由信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESNOSBASEROUTE
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

# DSP RESNOSBASEROUTE（查询NOS Base平面网络的路由信息）

## 功能

该命令用于查询NOS Base平面网络的路由信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源名称或容器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的资源的信息。使用<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>查看资源名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RESNOSBASEROUTE]] · NOS Base平面网络的路由信息（RESNOSBASEROUTE）

## 使用实例

- 查询VNFP的所有资源的NOS Base平面网络路由信息：
  ```
  DSP RESNOSBASEROUTE:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  资源名称  路由前缀      路由掩码  接口名称  范围  下一跳       

  OMU1      192.168.0.0   16        eth1      NULL  192.168.0.81  
  OMU1      172.30.118.0  24        eth1      NULL  192.168.0.81  
  OMU1      192.168.0.0   16        eth1      link  NULL         
  OMU2      192.168.0.0   16        eth1      NULL  192.168.0.65  
  OMU2      172.30.118.0  24        eth1      NULL  192.168.0.65  
  OMU2      192.168.0.0   16        eth1      link  NULL         
  (结果个数 = 6)

  ---    END
  ```

- 查询VNFP的指定“资源名称”为“OMU1”的NOS Base平面网络路由信息：
  ```
  DSP RESNOSBASEROUTE: RESNAME="OMU1";
  RETCODE = 0  操作成功

  结果如下:
  ---------
  资源名称  路由前缀      路由掩码  接口名称  范围  下一跳       

  OMU1      192.168.0.0   16        eth1      NULL  192.168.0.81  
  OMU1      172.30.118.0  24        eth1      NULL  192.168.0.81  
  OMU1      192.168.0.0   16        eth1      link   NULL         
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NOS-Base平面网络的路由信息（DSP-RESNOSBASEROUTE）_52236165.md`
