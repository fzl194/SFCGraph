---
id: UNC@20.15.2@MMLCommand@LST NGSRVPLMN
type: MMLCommand
name: LST NGSRVPLMN（查询5G Serving PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGSRVPLMN
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- Serving PLMN信息管理
status: active
---

# LST NGSRVPLMN（查询5G Serving PLMN）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于查询Serving PLMN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：可选参数<br>参数含义：该参数用于在系统内唯一标识一个PLMN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本PLMN所归属的运营商。NOID通过ADD NGMNO进行配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGSRVPLMN]] · 5G Serving PLMN（NGSRVPLMN）

## 使用实例

- 查询运营商（NOID为0）的Serving PLMN信息，执行如下命令：
  ```
  %%LST NGSRVPLMN: NOID=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    PLMN索引  =  0
  运营商标识  =  0
  移动国家码  =  460
    移动网号  =  03
    描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中的Serving PLMN信息，执行如下命令：
  ```
  %%LST NGSRVPLMN:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  PLMN索引  运营商标识  移动国家码  移动网号  描述信息  

  0           0         460         03        NULL         
  1           0         460         002       NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGSRVPLMN.md`
