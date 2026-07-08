---
id: UDG@20.15.2@MMLCommand@DSP RESNOSBASEIFSTAT
type: MMLCommand
name: DSP RESNOSBASEIFSTAT（查询NOS Base平面网络的报文统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RESNOSBASEIFSTAT
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

# DSP RESNOSBASEIFSTAT（查询NOS Base平面网络的报文统计信息）

## 功能

该命令用于查询NOS Base平面网络的报文统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 资源名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源名称或容器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的资源的信息。使用<br>[**DSP RES**](../../../系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)<br>查看资源名称。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RESNOSBASEIFSTAT]] · NOS Base平面网络的报文统计信息（RESNOSBASEIFSTAT）

## 使用实例

- 查询VNFP的所有资源的NOS Base平面网络报文统计信息：
  ```
  DSP RESNOSBASEIFSTAT:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  资源名称  接收的报文数目  接收的报文字节数(Bytes)  接收的错误报文数目  接收时丢弃的报文数目  接收的过载报文数目  接收的帧错误报文数目  发送的报文数目  发送的报文字节数(Bytes)  发送的错误报文数目  发送时丢弃的报文数目  发送的过载报文数目  发送的运载错误报文数目  发送的冲突报文数目 
  OMU1     9747414       2239571236 (2.0 GiB)   0                 0                  0                 0                 10855620       8535239905 (7.9 GiB)  0                 0                  0                 0                    0                   
  OMU2     4138344       1362664422 (1.2 GiB)   0                 0                  0                 0                 5092679        1265083915 (1.1 GiB)  0                 0                  0                 0                    0
  (结果个数 = 2)

  ---    END
  ```

- 查询VNFP的指定“资源名称”为“OMU1”的NOS Base平面网络报文统计信息：
  ```
  DSP RESNOSBASEIFSTAT: RESNAME="OMU1";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
                 资源名称  =  OMU1
           接收的报文数目  =  9747414
  接收的报文字节数(Bytes)  =  2239571236 (2.0 GiB)
       接收的错误报文数目  =  0
     接收时丢弃的报文数目  =  0
       接收的过载报文数目  =  0
     接收的帧错误报文数目  =  0
           发送的报文数目  =  10855620
  发送的报文字节数(Bytes)  =  8535239905 (7.9 GiB)
       发送的错误报文数目  =  0
     发送时丢弃的报文数目  =  0
       发送的过载报文数目  =  0
   发送的运载错误报文数目  =  0
       发送的冲突报文数目  =  0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RESNOSBASEIFSTAT.md`
