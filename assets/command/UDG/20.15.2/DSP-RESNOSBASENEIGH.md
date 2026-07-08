---
id: UDG@20.15.2@MMLCommand@DSP RESNOSBASENEIGH
type: MMLCommand
name: DSP RESNOSBASENEIGH（查询NOS Base平面网络的邻居信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESNOSBASENEIGH
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

# DSP RESNOSBASENEIGH（查询NOS Base平面网络的邻居信息）

## 功能

该命令用于查询NOS Base平面网络的邻居信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源名称或容器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的资源的信息。使用<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>查看资源名称。 |

## 操作的配置对象

- [NOS Base平面网络的邻居信息（RESNOSBASENEIGH）](configobject/UDG/20.15.2/RESNOSBASENEIGH.md)

## 使用实例

- 查询VNFP的所有资源的NOS Base平面网络邻居信息：
  ```
  DSP RESNOSBASENEIGH:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  资源名称  IP地址        接口名称  MAC地址            表项状态   

  OMU1      192.168.0.111  eth1      02:55:b8:17:00:6f  STALE      
  OMU1      192.168.0.88   eth1      02:55:b8:17:00:58  REACHABLE  
  OMU1      192.168.1.11   eth1      02:55:b8:17:01:0b  REACHABLE  
  OMU1      192.168.0.164  eth1      02:55:b8:17:00:a3  STALE      
  OMU1      192.168.0.136  eth1      02:55:b8:17:00:87  REACHABLE  
  OMU1      192.168.0.219  eth1      02:55:b8:17:00:da  STALE      
  OMU1      192.168.1.165  eth1      02:55:b8:17:01:a5  STALE      
  OMU1      192.168.0.209  eth1      02:55:b8:17:00:d0  REACHABLE  
  OMU1      192.168.0.197  eth1      02:55:b8:17:00:c5  STALE      
  OMU1      192.168.1.238  eth1      02:55:b8:17:01:e8  STALE      
  OMU1      192.168.1.225  eth1      02:55:b8:17:01:e0  REACHABLE  
  OMU1      192.168.1.228  eth1      02:55:b8:17:01:e4  STALE      
  OMU1      192.168.0.127  eth1      02:55:b8:17:00:7f  REACHABLE  
  OMU1      192.168.0.92   eth1      02:55:b8:17:00:5c  DELAY      
  OMU1      192.168.0.187  eth1      02:55:b8:17:00:bb  REACHABLE  
  OMU1      192.168.1.90   eth1      02:55:b8:17:01:54  STALE      
  OMU1      192.168.2.18   eth1      02:55:b8:17:02:12  STALE      
  OMU1      192.168.0.135  eth1      02:55:b8:17:00:87  REACHABLE  
  OMU1      192.168.0.235  eth1      02:55:b8:17:00:eb  REACHABLE  
  OMU1      192.168.0.238  eth1      02:55:b8:17:00:ee  REACHABLE  
  OMU1      192.168.0.225  eth1      02:55:b8:17:00:e1  STALE      
  OMU1      192.168.0.198  eth1      02:55:b8:17:00:c5  STALE      
  OMU1      192.168.0.118  eth1      02:55:b8:17:00:76  DELAY      
  OMU1      192.168.0.105  eth1      02:55:b8:17:00:69  STALE      
  OMU1      192.168.0.68   eth1      02:55:b8:17:00:44  REACHABLE  
  OMU1      192.168.0.178  eth1      02:55:b8:17:00:b2  STALE      
  OMU1      192.168.0.163  eth1      02:55:b8:17:00:a3  STALE      
  OMU1      192.168.0.153  eth1      02:55:b8:17:00:99  REACHABLE  
  OMU1      192.168.1.94   eth1      02:55:b8:17:01:5e  STALE      
  OMU1      192.168.1.81   eth1      02:55:b8:17:01:51  REACHABLE  
  OMU1      192.168.1.84   eth1      02:55:b8:17:01:54  STALE      
  OMU1      192.168.0.128  eth1      02:55:b8:17:00:80  REACHABLE  
  OMU1      192.168.0.226  eth1      02:55:b8:17:00:e1  STALE      
  OMU1      192.168.1.172  eth1      02:55:b8:17:01:ac  REACHABLE  
  OMU1      192.168.0.214  eth1      02:55:b8:17:00:d0  REACHABLE  
  OMU1      192.168.0.204  eth1      02:55:b8:17:00:c5  REACHABLE  
  OMU1      192.168.1.232  eth1      02:55:b8:17:01:e8  STALE      
  OMU1      192.168.1.7    eth1      02:55:b8:17:01:07  REACHABLE  
  OMU1      192.168.0.179  eth1      02:55:b8:17:00:b2  STALE      
  OMU1      192.168.2.28   eth1      02:55:b8:17:02:1c  STALE      
  OMU1      192.168.0.129  eth1      02:55:b8:17:00:80  REACHABLE  
  OMU1      192.168.1.188  eth1      02:55:b8:17:01:bc  STALE      
  OMU1      192.168.0.215  eth1      02:55:b8:17:00:d0  REACHABLE  
  OMU1      192.168.1.193  eth1      02:55:b8:17:01:c1  REACHABLE  
  OMU1      192.168.0.188  eth1      02:55:b8:17:00:bb  REACHABLE  
  OMU1      192.168.0.218  eth1      02:55:b8:17:00:da  STALE      
  OMU1      192.168.0.208  eth1      02:55:b8:17:00:d0  REACHABLE  
  OMU1      192.168.0.203  eth1      02:55:b8:17:00:c5  STALE      
  OMU1      192.168.1.224  eth1      02:55:b8:17:01:e0  REACHABLE  
  OMU1      192.168.1.194  eth1      02:55:b8:17:01:c2  STALE      
  OMU2      192.168.0.127  eth1      02:55:b8:17:00:7f  REACHABLE  
  OMU2      192.168.1.81   eth1      02:55:b8:17:01:51  REACHABLE  
  OMU2      192.168.1.194  eth1      02:55:b8:17:01:c2  STALE      
  OMU2      192.168.0.153  eth1      02:55:b8:17:00:99  REACHABLE  
  OMU2      192.168.0.235  eth1      02:55:b8:17:00:eb  REACHABLE  
  OMU2      192.168.1.184  eth1      02:55:b8:17:01:b8  REACHABLE  
  OMU2      192.168.0.76   eth1      02:55:b8:17:00:4c  STALE      
  OMU2      192.168.0.111  eth1      02:55:b8:17:00:6f  REACHABLE  
  OMU2      192.168.0.238  eth1      02:55:b8:17:00:ee  REACHABLE  
  (结果个数 = 59)

  ---    END
  ```

- 查询VNFP的指定“资源名称”为“OMU1”的NOS Base平面网络邻居信息：
  ```
  DSP RESNOSBASENEIGH: RESNAME="OMU1";
  RETCODE = 0  操作成功

  结果如下:
  ---------
  资源名称  IP地址        接口名称  MAC地址            表项状态   

  OMU1      192.168.0.111  eth1      02:55:b8:17:00:6f  STALE      
  OMU1      192.168.0.88   eth1      02:55:b8:17:00:58  REACHABLE  
  OMU1      192.168.1.11   eth1      02:55:b8:17:01:0b  STALE      
  OMU1      192.168.0.164  eth1      02:55:b8:17:00:a3  STALE      
  OMU1      192.168.0.136  eth1      02:55:b8:17:00:87  REACHABLE  
  OMU1      192.168.0.219  eth1      02:55:b8:17:00:da  STALE      
  OMU1      192.168.1.165  eth1      02:55:b8:17:01:a5  STALE      
  OMU1      192.168.0.209  eth1      02:55:b8:17:00:d0  REACHABLE  
  OMU1      192.168.0.197  eth1      02:55:b8:17:00:c5  STALE      
  OMU1      192.168.1.238  eth1      02:55:b8:17:01:e8  STALE      
  OMU1      192.168.1.225  eth1      02:55:b8:17:01:e0  REACHABLE  
  OMU1      192.168.1.228  eth1      02:55:b8:17:01:e4  STALE      
  OMU1      192.168.0.127  eth1      02:55:b8:17:00:7f  REACHABLE  
  OMU1      192.168.0.92   eth1      02:55:b8:17:00:5c  STALE      
  OMU1      192.168.0.187  eth1      02:55:b8:17:00:bb  REACHABLE  
  OMU1      192.168.1.90   eth1      02:55:b8:17:01:54  STALE      
  OMU1      192.168.2.18   eth1      02:55:b8:17:02:12  STALE      
  OMU1      192.168.0.135  eth1      02:55:b8:17:00:87  REACHABLE  
  OMU1      192.168.0.235  eth1      02:55:b8:17:00:eb  REACHABLE  
  OMU1      192.168.0.238  eth1      02:55:b8:17:00:ee  REACHABLE  
  OMU1      192.168.0.225  eth1      02:55:b8:17:00:e1  STALE      
  OMU1      192.168.0.198  eth1      02:55:b8:17:00:c5  STALE      
  OMU1      192.168.0.118  eth1      02:55:b8:17:00:76  REACHABLE  
  OMU1      192.168.0.105  eth1      02:55:b8:17:00:69  STALE      
  OMU1      192.168.0.68   eth1      02:55:b8:17:00:44  REACHABLE  
  OMU1      192.168.0.178  eth1      02:55:b8:17:00:b2  STALE      
  OMU1      192.168.0.163  eth1      02:55:b8:17:00:a3  STALE      
  OMU1      192.168.0.153  eth1      02:55:b8:17:00:99  REACHABLE  
  OMU1      192.168.1.94   eth1      02:55:b8:17:01:5e  STALE      
  OMU1      192.168.1.81   eth1      02:55:b8:17:01:51  REACHABLE  
  OMU1      192.168.1.84   eth1      02:55:b8:17:01:54  STALE      
  OMU1      192.168.0.128  eth1      02:55:b8:17:00:80  REACHABLE  
  OMU1      192.168.0.226  eth1      02:55:b8:17:00:e1  STALE      
  OMU1      192.168.1.172  eth1      02:55:b8:17:01:ac  DELAY      
  OMU1      192.168.0.214  eth1      02:55:b8:17:00:d0  REACHABLE  
  OMU1      192.168.0.204  eth1      02:55:b8:17:00:c5  REACHABLE  
  OMU1      192.168.1.232  eth1      02:55:b8:17:01:e8  STALE      
  OMU1      192.168.1.7    eth1      02:55:b8:17:01:07  REACHABLE  
  OMU1      192.168.0.179  eth1      02:55:b8:17:00:b2  STALE      
  OMU1      192.168.2.28   eth1      02:55:b8:17:02:1c  STALE      
  OMU1      192.168.0.129  eth1      02:55:b8:17:00:80  REACHABLE  
  OMU1      192.168.1.188  eth1      02:55:b8:17:01:bc  STALE      
  OMU1      192.168.0.215  eth1      02:55:b8:17:00:d0  STALE      
  OMU1      192.168.1.193  eth1      02:55:b8:17:01:c1  REACHABLE  
  OMU1      192.168.0.188  eth1      02:55:b8:17:00:bb  REACHABLE  
  OMU1      192.168.0.218  eth1      02:55:b8:17:00:da  STALE      
  OMU1      192.168.0.208  eth1      02:55:b8:17:00:d0  REACHABLE  
  OMU1      192.168.0.203  eth1      02:55:b8:17:00:c5  STALE      
  OMU1      192.168.1.224  eth1      02:55:b8:17:01:e0  REACHABLE  
  OMU1      192.168.1.194  eth1      02:55:b8:17:01:c2  STALE      
  (结果个数 = 50)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NOS-Base平面网络的邻居信息（DSP-RESNOSBASENEIGH）_52116461.md`
