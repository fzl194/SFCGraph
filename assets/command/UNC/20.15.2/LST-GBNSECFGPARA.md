---
id: UNC@20.15.2@MMLCommand@LST GBNSECFGPARA
type: MMLCommand
name: LST GBNSECFGPARA（查询NSE属性模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBNSECFGPARA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- NSE属性模板管理
status: active
---

# LST GBNSECFGPARA（查询NSE属性模板）

## 功能

**适用网元：SGSN**

此命令用于查询NSE属性模板。

## 注意事项

- 此命令执行后立即生效。
- 若不输入参数，则查询所有NSE属性模板。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAINDEX | 模板索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的NSE属性模板的索引。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBNSECFGPARA]] · NSE属性模板（GBNSECFGPARA）

## 使用实例

1. 查询所有NSE属性模板：
  LST GBNSECFGPARA:;
  ```
  %%LST GBNSECFGPARA:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   模板索引  FLUSH监控定时器（ms）  是否支持PFC  是否支持CBL  是否支持INR  是否支持LCS  是否支持RIM  是否携带ARP信元  是否携带RA Capability信元  是否支持Gb-Flex  是否支持特殊业务类型  BSS支持的Qos版本  本端端点个数      信令权重  数据权重  是否支持MOCN  是否支持SPID

   0         50                     是           是           是           否           否           否               否                         否               否                    R99               系统内业务IP个数  255       255       否            否
   1         2000                   否           否           否           是           是           是               是                         是               是                    R5                6                 255       255       否            否
  (结果个数 = 2)
  ---    END
  ```
2. 查询 “ 模板索引 ” 为 “0” 的NSE属性模板：
  LST GBNSECFGPARA:PARAINDEX=0;
  ```
  %%LST GBNSECFGPARA:PARAINDEX=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
                   模板索引  =  0
      FLUSH监控定时器（ms）  =  50
                是否支持PFC  =  是
                是否支持CBL  =  是
                是否支持INR  =  是
                是否支持LCS  =  否
                是否支持RIM  =  否
            是否携带ARP信元  =  否
  是否携带RA Capability信元  =  否
            是否支持Gb-Flex  =  否
       是否支持特殊业务类型  =  否
           BSS支持的Qos版本  =  R99
               本端端点个数  =  系统内业务IP个数
                   信令权重  =  255
                   数据权重  =  255
               是否支持MOCN  =  否
  	     是否支持SPID  =  否
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GBNSECFGPARA.md`
