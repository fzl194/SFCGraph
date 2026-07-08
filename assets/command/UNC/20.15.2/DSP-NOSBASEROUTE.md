---
id: UNC@20.15.2@MMLCommand@DSP NOSBASEROUTE
type: MMLCommand
name: DSP NOSBASEROUTE（查询NOS Base平面网络的路由信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NOSBASEROUTE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 基础网络调测
status: active
---

# DSP NOSBASEROUTE（查询NOS Base平面网络的路由信息）

## 功能

该命令用于查询NOS Base平面网络的路由信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的RU的信息。使用<br>[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NOSBASEROUTE]] · NOS Base平面网络的路由信息（NOSBASEROUTE）

## 使用实例

- 查询指定大颗粒服务实例的所有NOS Base平面网络路由信息：
  ```
  DSP NOSBASEROUTE: SERVICEINSTANCE="CSDB_VNFC_999";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  RU名称           路由前缀      路由掩码  接口名称  范围  下一跳        

  CSDB_OM_RU_0001  192.168.0.0   16        eth1      NULL  192.168.0.81   
  CSDB_OM_RU_0001  172.30.118.0  24        eth1      NULL  192.168.0.81   
  CSDB_OM_RU_0001  192.168.0.0   16        eth1      link  NULL          
  CSDB_OM_RU_0002  192.168.0.0   16        eth1      NULL  192.168.0.65   
  CSDB_OM_RU_0002  172.30.118.0  24        eth1      NULL  192.168.0.65   
  CSDB_OM_RU_0002  192.168.0.0   16        eth1      link  NULL          
  CSDB_SD_RU_0064  192.168.0.0   16        eth1      NULL  192.168.1.145  
  CSDB_SD_RU_0064  172.30.118.0  24        eth1      NULL  192.168.1.145  
  CSDB_SD_RU_0064  192.168.0.0   16        eth1      link  NULL          
  CSDB_SD_RU_0065  192.168.0.0   16        eth1      NULL  192.168.1.129  
  CSDB_SD_RU_0065  172.30.118.0  24        eth1      NULL  192.168.1.129  
  CSDB_SD_RU_0065  192.168.0.0   16        eth1      link  NULL          
  (结果个数 = 12)

  ---    END
  ```

- 查询指定大颗粒服务实例的指定RU名称为“CSDB_SD_RU_0064”的NOS Base平面网络路由信息：
  ```
  DSP NOSBASEROUTE: RUNAME="CSDB_SD_RU_0064", SERVICEINSTANCE="CSDB_VNFC_999";
  RETCODE = 0  操作成功

  结果如下:
  ---------
  RU名称           路由前缀      路由掩码  接口名称  范围  下一跳        

  CSDB_SD_RU_0064  192.168.0.0   16        eth1      NULL  192.168.1.145  
  CSDB_SD_RU_0064  172.30.118.0  24        eth1      NULL  192.168.1.145  
  CSDB_SD_RU_0064  192.168.0.0   16        eth1      link  NULL          
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NOSBASEROUTE.md`
