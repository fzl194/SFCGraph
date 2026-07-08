# 查询单协议推理配置（LST INSAPROTPARA）

- [命令功能](#ZH-CN_CONCEPT_0000206756165568__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206756165568__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206756165568__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206756165568__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206756165568__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206756165568__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206756165568)

**适用NF：PGW-U、UPF**

查询单协议推理配置。

#### [注意事项](#ZH-CN_CONCEPT_0000206756165568)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206756165568)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206756165568)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示协议组包含的协议的名字。<br>数据来源：本端规划<br>取值范围：1、字符串类型，输入长度范围为1～31; 2、不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置协议前需使用工程命令smctrldsp protocol-list sub-protocol查询三级协议表；使用MML命令DSP CFGTABLEDATA: OMUTYPE=master, DBTYPE=running, QUERYTYPE=table-data, TABLENAME="AISAppProtocol", SERVICEINSTANCE="ACS";查询INSA自定义协议表。 |

#### [使用实例](#ZH-CN_CONCEPT_0000206756165568)

- 查询当前单个协议http的相关参数配置：
  ```
  LST INSAPROTPARA:PROTOCOLNAME="http";
  ```
  ```

  RETCODE = 0 操作成功。

  单协议推理配置信息
  ------
                             协议名称 = http
                  智能识别推理能力开关 = Enable
           智能识别结果用于策略匹配开关 = Enable
                  智能识别阈值(千分比) = 600

  (结果个数 = 1)
  --- END
  ```
- 查询当前所有添加协议的相关参数配置：
  ```
  LST INSAPROTPARA:;
  ```
  ```

  RETCODE = 0 操作成功。

  单协议推理配置信息
  ------
     协议名称      智能识别推理能力开关    智能识别结果用于策略匹配开关    智能识别阈值(千分比)
      http             Enable                  Enable                    600
      https            Inherit                 Inherit                   600

  (结果个数 = 2)
  --- END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206756165568)

参见ADD INSAPROTPARA的参数说明。
