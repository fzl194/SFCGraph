---
id: UNC@20.15.2@MMLCommand@LST DNNTAISSP
type: MMLCommand
name: LST DNNTAISSP（查询DNN的TAI和ServingScope映射）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNNTAISSP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- 配置DNN的TAI和ServingScope映射
status: active
---

# LST DNNTAISSP（查询DNN的TAI和ServingScope映射）

## 功能

**适用NF：AMF**

该命令用于查询DNN的TAI和ServingScope映射。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNN网络标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。输入指定的DNN NI，可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNTAISSP]] · DNN的TAI和ServingScope映射（DNNTAISSP）

## 使用实例

- 查询一条“DNN网络标识”为“huawei.com”的TAI和ServingScope映射关系，执行如下命令：
  ```
  +++    UNC/*MEID:0 MENAME:unc*/        2023-05-17 10:36:34+8:00
  O&M    #7520
  %%LST DNNTAISSP: DNNNI="HUAWEI.COM";%%
  RETCODE = 0  操作成功

  输出结果如下
  ------------------------
     DNN网络标识  =  HUAWEI.COM
             MCC  =  460
             MNC  =  03
  跟踪区起始编码  =  000112
  跟踪区结束编码  =  000700
        服务范围  =  puxi:pudong
  (结果个数 = 1)

  ---    END
  ```
- 查询所有DNN的TAI和ServingScope映射关系，执行如下命令：
  ```
  +++    UNC/*MEID:0 MENAME:unc*/        2023-05-17 10:36:41+8:00
  O&M    #7521
  %%LST DNNTAISSP:;%%
  RETCODE = 0  Operation succeeded

  The result is as follows
  ------------------------
  DNN网络标识  MCC  MNC  跟踪区起始编码  跟踪区结束编码  服务范围  

  BEIJING.CY   460  03   000800          000999          pudong:puxi    
  HUAWEI.COM   460  03   000112          000700          puxi:pudong    
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNNTAISSP.md`
